import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft()
mc.postToChat("Get Block")
x, y, z = mc.player.getPos()
print('player position:', str(x), str(y), str(z))
print(mc.getBlock(x, y, z))
print(mc.getBlocks(x-10, y-10,z-10,x+10, y+10,z+10))
# mc.getBlocks()
