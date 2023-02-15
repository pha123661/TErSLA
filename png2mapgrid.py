import numpy as np
from PIL import Image

# img = Image.open('map.png').convert('L')
# img = np.array(img)
# img = ((255 - img) == 255).astype(int)

# H, W = img.shape[0], img.shape[1]
# if W > H:
#     img = np.concatenate([
#         img,
#         np.zeros((W - H, W))
#     ])
# elif W < H:
#     img = np.concatenate([
#         img,
#         np.zeros((H, H - W))
#     ], axis=1)
# img = img[:-3, 3:]
# np.savetxt("map_config.txt", img, fmt="%d")

# map_ez = np.zeros((40, 40), dtype=int)
# map_ez[:, 0] = 1
# map_ez[:, -1] = 1
# map_ez[0, :] = 1
# map_ez[-1, :] = 1
# np.savetxt("map_config_ez.txt", map_ez, fmt="%d")

# img = Image.open('map.png').convert('L')
# img = np.array(img)
# img = ((255 - img) == 255).astype(int)

img = Image.open('map_mid.png').convert('L')
img = np.array(img)
img = ((255 - img) == 255).astype(int)

H, W = img.shape[0], img.shape[1]
if W > H:
    img = np.concatenate([
        img,
        np.zeros((W - H, W))
    ])
elif W < H:
    img = np.concatenate([
        img,
        np.zeros((H, H - W))
    ], axis=1)
np.savetxt("map_config_mid.txt", img, fmt="%d")
