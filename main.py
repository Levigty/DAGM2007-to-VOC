import os
import glob
import ntpath
import cover_dataset

# The filename of the download dataset
data_dir = 'raw_dataset'
# The folder name you want to save the VOC format dataset
save_dir = 'DAGM2007_VOC'

EXPECTED_DEFECTIVE_SAMPLES_PER_CLASS = {
    "Train": {
        1: 79, 2: 66, 3: 66, 4: 82, 5: 70,
        6: 83, 7: 150, 8: 150, 9: 150, 10: 150,
    },
    "Test": {
        1: 71, 2: 84, 3: 84, 4: 68, 5: 80,
        6: 67, 7: 150, 8: 150, 9: 150, 10: 150,
    }
}


if __name__ == '__main__':
    voc_train_ann, voc_train_jpg, voc_test_ann, voc_test_jpg = cover_dataset.create_save_folder(save_dir=save_dir)
    train_num = 0
    test_num = 0
    for class_id in range(10):
        # It depends on your own folder
        class_name = "Class%d" % (class_id + 1)
        class_folder_path = os.path.join(data_dir, class_name)

        print("\n[DAGM Preprocessing] Parsing Class ID: %02d ..." % (class_id + 1))

        for data_set in ["Train", "Test"]:

            num_sample = 0

            class_set_folder_path = os.path.join(class_folder_path, data_set)

            img_files = glob.glob(os.path.join(class_set_folder_path, "*.PNG"))

            for file in img_files:

                filepath, fullname = ntpath.split(file)

                filename, extension = os.path.splitext(os.path.basename(fullname))

                lbl_filename = "%s_label.PNG" % filename
                lbl_filepath = os.path.join(filepath, "Label", lbl_filename)

                # We ignore the images without defects.
                # Only if the image contains defects, we use it to construct dataset
                if os.path.exists(lbl_filepath):
                    num_sample += 1
                    img_id = lbl_filepath[-14:-10]
                    if data_set == "Train":
                        train_num += 1
                        cover_dataset.write_img(class_set_folder_path, img_id, voc_train_jpg, num_sample)
                        cover_dataset.create_xml_file(lbl_filepath, voc_train_ann, num_sample, class_name)
                    else:
                        test_num += 1
                        cover_dataset.write_img(class_set_folder_path, img_id, voc_test_jpg, num_sample)
                        cover_dataset.create_xml_file(lbl_filepath, voc_test_ann, num_sample, class_name)

            # Ensure the num of defect images is correct
            if num_sample != EXPECTED_DEFECTIVE_SAMPLES_PER_CLASS[data_set][class_id + 1]:
                raise RuntimeError("There should be `%d` defective samples instead of `%d` in challenge (%s): %d" % (
                    EXPECTED_DEFECTIVE_SAMPLES_PER_CLASS[data_set][class_id + 1],
                    num_sample, data_set, class_id + 1))

            # Display the proposs
            cover_dataset.view_bar([data_set + ' Conversion progress:'], num_sample,
                                   EXPECTED_DEFECTIVE_SAMPLES_PER_CLASS[data_set][class_id + 1])
