class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = rooms[0]
        rooms[0] = []
        unvisited_rooms = set(range(1,len(rooms)))
        
        while len(keys) > 0 and len(unvisited_rooms) > 0:
            room_index = keys.pop()
            unvisited_rooms -= {room_index}
            next_keys = rooms[room_index]
            rooms[room_index] = []
            for key in next_keys:
                keys.append(key)
        
        return not unvisited_rooms