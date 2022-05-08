
import json
import numpy as np

def convert(filename):
    with open(filename)as f: 
        data = json.load(f)
    
    images = data["images"]
    annotation_index = 0    
    annotations = data["annotations"]
    for i, image in enumerate(images):
        current_annotations = ""
        image_id = image["id"]
        w = image["width"]
        h = image["height"]
        file_name = image["file_name"]
        label_file_name = "labels/" + '/'.join(file_name.split("/")[1:])[:-3] + "txt"
        print(label_file_name)
        while annotations[annotation_index]["image_id"] == image_id:
            annotation = annotations[annotation_index]
            class_index = annotation["category_id"]-1
            bbox = np.array(annotation["bbox"])
            bbox[[0,2]] /= w
            bbox[[1,3]] /= h
            if class_index > 7:
                print("ERROR")
            current_annotations += str(class_index)
            for b in bbox:
                current_annotations += " " + str(b)

            current_annotations += "\n" 
            if annotation_index < len(annotations) -1:
                annotation_index += 1
            else:
                break

        with open(label_file_name, "w") as file:
            file.write(current_annotations)


if __name__ == "__main__":
    convert("val_annotations.json")
    convert("train_annotations.json")
