import os
import sys

import justGo as gen

def generate_change_tag():
    dic = {
        "face":0,
        "portrait":0,
        "hair_between_eyes":0,
        "border":0,
        "smile":0,
        "black_border":0,
        "long_hair":0,
        "upper_body":0,
        "letterboxed":0,
        "sketch":0,
        "close-up":0,
        "short_hair":2,
        "simple_background":0,
        "closed_mouth":0,
        "eyebrows":0,
        "brown_hair":0,
        "shirt":0,
        "bow":0,
        "open_mouth":0,
        "eyelashes":0,
        "ribbon":0,
        "white_background":0,
        "lips":0,
        "red_eyes":0,
        "brown_eyes":0,
        "hair_bow":0,
        "shiny_hair":0,
        "pillarboxed":0,
        "parted_lips":0,
        "collarbone":0,
        "white_shirt":0,
        "blonde_hair":0,
        "sidelocks":0,
        "hair_ornament":0,
        "circle_cut":0,
        "shiny":0,
        "blue_eyes":0,
        "animal_ears":0,
        "purple_eyes":0,
        ":d":0,
        ":o":0,
        "hat":0,
        "yellow_eyes":0,
        "jewelry":0,
        "hair_ribbon":0,
        "orange_eyes":0,
        "bare_shoulders":0,
        "traditional_media":0,
        "rain":0,
        "twintails":0,
        "tears":0,
        "ahoge":0,
        "black_hair":0,
        "green_eyes":0,
        "signature":0,
        "heart":0,
        "purple_hair":0,
        "fang":0,
        "pink_hair":0,
        "holding":0,
        "shikishi":0,
        "frame":0,
        "pink_eyes":0,
        "nose_blush":0,
        "collared_shirt":0,
        "red_hair":0,
        "gloves":0,
        "eyes_visible_through_hair":0,
        "orange_hair":0,
        "artist_name":0,
        "pink_lips":0,
        "expressionless":0,
        "silver_hair":0,
        "long_sleeves":0,
        "outdoors":0,
        "blunt_bangs":0,
        "dress":0,
        "choker":0,
        "teeth":0,
        "frills":0,
        "striped":0,
        "pink_background":0,
        "wing_collar":0,
        "cat_ears":0,
        "school_uniform":0,
        "grey_background":0,
        "gradient_background":0,
        "sleeveless":0,
        "symbol-shaped_pupils":0,
        "hair_intakes":0,
        "blue_background":0,
        "hairband":0,
        "red_bow":0,
        "breasts":0,
        "photo":0,
        "transparent_background":0,
        "fingernails":0,
        "aqua_eyes":0,
        "food":0,
        "gradient":0,
        "ponytail":0,
        "necktie":0,
        "light_brown_hair":0,
        "flower":0,
        "yellow_background":0,
        "jacket":0
    }
    return dic

if __name__ == '__main__':
    tag = generate_change_tag()
    user_id = "10000001"
    truncated = 0.7
    gen.init_modif(truncated, user_id, tag)