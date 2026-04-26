import csv
import time
from typing import Iterable, Callable, Optional, Dict, Any, List
import can

class AdlerWolfBLFTools:
    """Backend BLF utilities without UI."""

    def read(self, path:str):
        with can.BLFReader(path) as reader:
            for msg in reader:
                yield msg

    def to_dict(self, msg) -> Dict[str, Any]:
        return {
            'timestamp': msg.timestamp,
            'channel': getattr(msg, 'channel', 0),
            'id': msg.arbitration_id,
            'hex_id': hex(msg.arbitration_id),
            'extended': msg.is_extended_id,
            'fd': getattr(msg, 'is_fd', False),
            'brs': getattr(msg, 'bitrate_switch', False),
            'esi': getattr(msg, 'error_state_indicator', False),
            'dlc': msg.dlc,
            'data': bytes(msg.data),
            'data_hex': msg.data.hex().upper(),
        }

    def filter_id(self, path:str, can_id:int):
        for msg in self.read(path):
            if msg.arbitration_id == can_id:
                yield msg

    def export_csv(self, blf_path:str, csv_path:str):
        with open(csv_path, 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(['timestamp','channel','id','extended','fd','brs','esi','dlc','data_hex'])
            for msg in self.read(blf_path):
                d = self.to_dict(msg)
                w.writerow([d['timestamp'], d['channel'], d['hex_id'], d['extended'], d['fd'], d['brs'], d['esi'], d['dlc'], d['data_hex']])

    def copy(self, src:str, dst:str):
        writer = can.BLFWriter(dst)
        try:
            for msg in self.read(src):
                writer.on_message_received(msg)
        finally:
            writer.stop()

    def write_messages(self, dst:str, messages:Iterable):
        writer = can.BLFWriter(dst)
        try:
            for msg in messages:
                writer.on_message_received(msg)
        finally:
            writer.stop()

    def replay(self, path:str, callback:Callable, realtime:bool=True):
        prev = None
        for msg in self.read(path):
            if realtime and prev is not None:
                delta = max(0, msg.timestamp - prev)
                time.sleep(delta)
            callback(msg)
            prev = msg.timestamp

    def decode_with_dbc(self, path:str, db):
        """db = cantools.database.load_file(...)"""
        for msg in self.read(path):
            try:
                decoded = db.decode_message(msg.arbitration_id, msg.data)
                yield msg, decoded
            except Exception:
                continue

    def stats(self, path:str) -> Dict[str, Any]:
        total = 0
        ids = {}
        fd = 0
        for msg in self.read(path):
            total += 1
            ids[msg.arbitration_id] = ids.get(msg.arbitration_id, 0) + 1
            if getattr(msg, 'is_fd', False):
                fd += 1
        return {
            'total_frames': total,
            'unique_ids': len(ids),
            'fd_frames': fd,
            'top_ids': sorted(ids.items(), key=lambda x: x[1], reverse=True)[:10]
        }

# Example usage:
# tool = AdlerWolfBLFTools()
# tool.export_csv('in.blf', 'out.csv')
# print(tool.stats('in.blf'))
