from imagekit import ImageSpec
from imagekit.processors import ResizeToFit


class ResizeImage(ImageSpec):
    processors = [ResizeToFit(900, 300)]
    format = 'JPEG'
    options = {'quality': 100}

    @staticmethod
    def resize_image(source):
        resized_image = ResizeImage(source=open(source))
        result = resized_image.generate()
        return result

    @staticmethod
    def save_resized_image(image_file, destination):
        dest = open(destination, 'wb')
        dest.write(image_file.read())
        dest.close()

    @staticmethod
    def resize_and_save_image(source, destination):
        temp_image_file = ResizeImage.resize_image(source)
        ResizeImage.save_resized_image(image_file=temp_image_file, destination=destination)