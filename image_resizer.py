from PIL import Image
import os

SIZE =[
24,32,64,128,512,1000
]

def generateOutputDir(name):
    print("Creting output dir: "+name)
    if not (os.path.exists("output_files/"+name)):
        os.makedirs("output_files/"+name)



def main():
    image_path = input("Please enter full path of image: \n")
    try:
        image = Image.open(image_path)
    except:
        print("Invalid image name")
        return 0
    input_image_size = image.size
    input_image_ratio = input_image_size[1]/input_image_size[0]
    print(f"Original size : {input_image_size}")
    print(f"Image Ratio : {input_image_ratio}")

    if os.path.exists(image_path):
        print("Processing")
        if os.path.exists("output_files"):
            print("Using existing output directory")
        else:
            print("Output directory doesnt exist. Creating...")
            os.makedirs("output_files")

        use_default = input("Use Default sizes(Y/N) \n")
        if use_default in ["Y","y"]:
            print("Using default image size")
            generateOutputDir("resize_def")
            for s in SIZE:
                image_size_h = s
                image_size_w = round(s / input_image_ratio)
                print("Height: ", image_size_h,"Width: ", image_size_w)
                resized = image.resize((int(image_size_w), int(image_size_h)))
                resized.save('output_files/resize_def/resized_{}X{}.png'.format(image_size_h, image_size_w))
                print("file saved as output_files/resize_def/resized_{}x{}.png".format(image_size_h, image_size_w))

        elif use_default in ["N","n"]:
            image_size_h = input("Enter required height: \n")
            image_size_w = input("Enter required width: \n")
            resized = image.resize((int(image_size_w), int(image_size_h)))
            generateOutputDir("resize_custom")
            resized.save('output_files/resize_custom/resized_{}X{}.png'.format(image_size_h,image_size_w))
            print("file saved as output_files/resize_custom/resized_{}x{}.png".format(image_size_h,image_size_w))
        else:
            print("Invalid selection. Retry")


    else:

        print("Image not found")


if __name__ == '__main__':
    main()