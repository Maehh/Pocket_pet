
from animal import animal_generator as animal

def unpack_animals(label_entry):
    text = ''
    temp_dog = animal(label_entry.get())
    for key, item in vars(temp_dog).items():
        text += f'{key}: {item} \n'
    return text