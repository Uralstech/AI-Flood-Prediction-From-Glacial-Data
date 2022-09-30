from PIL import Image
train_data = []
test_data = []

def get_data(idx, path, train=True):
    global train_data
    global test_data
    'D:\\Code\\python\\SnowAI test\\Map for AI\\'
    img = Image.open(f'{path}{idx+1}.jpg')
    pix = list(img.getdata())

    white = 0
    for i in range(len(pix)):
        pix[i] = [round(j/255, 3) for j in pix[i]]
    
        if pix[i][0] >= 0.827 and pix[i][1] >= 0.827 and pix[i][2] >= 0.827: white += 1

    if train: train_data.append((white / len(pix)) * 100)
    else: test_data.append((white / len(pix)) * 100)

for idx in range(16): get_data(idx, 'D:\\Code\\python\\SnowAI test\\Map for AI\\')
for idx in range(4): get_data(idx, 'D:\\Code\\python\\SnowAI test\\Map for AI\\t', False)

