import gdown
import zipfile
import os

# cwd = os.getcwd()

file_ids = [
    		# "11UGV3nbVv1x9IC--_tK3Uxf7hA6rlbsS",
            # "1VYz4q7GMy_mejgEpKK1Z1oSSw8E_Udmq",
            # "1WvYqJT4MmNI5WHMsBiBcMLm07TP6XsFQ",
            "14KX6VqF69MdSPk3Tr9PlDYbq7ArpdNUW",
            "1q36RaTZnpHVl4vRuNypoEMVWiiwCqhuD",
            "15zP8BP-5IvWXWZoYTNdvUJUiBqZ1hxu1"]

output_name = [
    	# "widerface.zip",
        # "MPSGaze_val.zip",
        # "MPSGaze_train.zip",
        "Resnet50_Final.pth",
        "mobilenetV1X0.25_pretrain.tar",
        "mobilenet0.25_Final.pth"]
for file_id, output in zip(file_ids, output_name):
    if os.path.exists(os.path.join(output)):
        continue
    gdown.download( f"https://drive.google.com/uc?export=download&confirm=pbef&id={file_id}", output)
    if ".zip" in output:
        with zipfile.ZipFile(output, 'r') as zip_ref:
            zip_ref.extractall(output.replace(".zip", ""))