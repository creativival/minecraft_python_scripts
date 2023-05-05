"""
正方形
"""
import mcpi.minecraft as minecraft
import mcpi.block as block

HALF_LENGTH = 3
BLOCK_ID = 1

mc = minecraft.Minecraft()
mc.postToChat("Set square")
x, y, z = map(int, mc.player.getPos())
print(f'player position: {x}:{y}:{z}')

x0, y0, z0 = x - HALF_LENGTH, y - HALF_LENGTH, z
# print(block_ids)
for i in range(HALF_LENGTH * 2):
    for j in range(HALF_LENGTH * 2):
        x1 = x0 + i
        y1 = y0 + 7
        z1 = z0 + j
        mc.setBlock(x1, y1, z1, BLOCK_ID)
