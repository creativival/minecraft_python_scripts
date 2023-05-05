"""
屋根
"""
import mcpi.minecraft as minecraft
import mcpi.block as block

HALF_LENGTH = 6
BLOCK_ID = 45

mc = minecraft.Minecraft()
mc.postToChat("Set roofs")
x, y, z = map(int, mc.player.getPos())
print(f'player position: {x}:{y}:{z}')

# x0, y0, z0 = x - HALF_LENGTH, y - HALF_LENGTH, z
# # print(block_ids)
# for i in range(HALF_LENGTH * 2):
#     for j in range(HALF_LENGTH * 2):
#         x1 = x0 + i
#         y1 = y0 + 7
#         z1 = z0 + j
#         mc.setBlock(x1, y1, z1, BLOCK_ID)

for times in range(10):
    for i in range(HALF_LENGTH):
        half_length = (HALF_LENGTH - i)
        full_length = half_length * 2
        x0, y0, z0 = x - half_length, y + i + times * 5, z - half_length
        for j in range(full_length):
            for k in range(full_length):
                x1 = x0 + j
                y1 = y0 + 3
                z1 = z0 + k
                mc.setBlock(x1, y1, z1, BLOCK_ID)

