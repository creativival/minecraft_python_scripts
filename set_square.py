"""
範囲内のブロックをすべて変更
"""
import mcpi.minecraft as minecraft
import mcpi.block as block

RANGE = 100
BLOCK_ID_TO_CHANGE = 20

mc = minecraft.Minecraft()
mc.postToChat("Change all blocks")
x, y, z = map(int, mc.player.getPos())
print(f'player position: {x}:{y}:{z}')

block_ids = mc.getBlocks(x-RANGE,y,z-RANGE,x+RANGE,y+RANGE,z+RANGE)
# print(block_ids)
for i in range(RANGE + 1):
    for j in range(RANGE * 2 + 1):
        for k in range(RANGE * 2 + 1):
            x1 = x - RANGE + j
            y1 = y + i
            z1 = z - RANGE + k
            block_id = block_ids[k + (j * (RANGE * 2 + 1)) + (i * (RANGE * 2 + 1)**2)]
            # print(f'position: {x1}:{y1}:{z1}:{block_id}')
            if block_id != 0:
                mc.setBlock(x1, y1, z1, BLOCK_ID_TO_CHANGE)
