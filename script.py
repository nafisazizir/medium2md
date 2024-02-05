import os
import requests


def download_image(url, save_path):
    response = requests.get(url)
    with open(save_path, "wb") as file:
        file.write(response.content)


def make_or_empty_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    else:
        for file_name in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file_name)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")


def modify_md_file(input_file, output_path, output_file):
    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    make_or_empty_dir(output_path)

    length = len(lines)

    for i, line in enumerate(lines):
        if "https://miro.medium.com" in line:
            image_url = line.split("\n")[0]
            if image_url[0] == "!":
                image_url = image_url[1:]

            filename = image_url.split("*")[-1]

            # file extension doesn't exist
            if not "." in filename:
                filename += ".png"

            new_line = f'![ ]({filename} " ")\n'

            # If image alt exist, put image alt in the Markdown
            if i + 2 < length and len(lines[i + 2]) < 70:
                image_alt = lines[i + 2].split("\n")[0]
                new_line = f'![{image_alt}]({filename} "{image_alt}")\n'
                lines[i + 2] = ""

            download_image(image_url, os.path.join(output_path, filename))
            lines[i] = new_line

    with open(os.path.join(output_path, output_file), "w", encoding="utf-8") as file:
        file.writelines(lines)


if __name__ == "__main__":
    # Output path should have suffix "/"
    output_path = "./output/"
    input_md_file = "input.md"
    output_md_file = "output.md"
    modify_md_file(input_md_file, output_path, output_md_file)
