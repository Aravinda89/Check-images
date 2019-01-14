def check_missing_files(images):
    """
    Check any file is missing
    :param images:List of images paths
    :return:
    """
    for inx, img in enumerate(images):
        try:
            print(inx, '/', len(images))
            fh = open(img, 'r')
        except FileNotFoundError:
            print("Can't find", img)
            break
    return
