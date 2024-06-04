

def pluralize_str(total_images):
    if ((total_images % 10) in [0, 5, 6, 7, 8, 9]) or ((total_images % 100) in [11, 12, 13, 14]):
        return 'картинок'
    elif total_images % 10 == 1:
        return 'картинку'
    elif total_images in [2,3,4]:
        return 'картинки'
    return 'картинок'
