"""
Author: Crichard25
Date: 14/7/2023
This is the components.py module.
Usage:
- Preparing Data for Training
"""

import tensorflow as tf
import tensorflow_transform as tft

# =========== GLOBAL VAR ===========
CATEGORICAL_FEATURES = {
    "gender": 3,
    "hypertension": 2,
    "heart_disease": 2,
    "ever_married": 2,
    "Residence_type": 2,
    "work_type": 5,
    "smoking_status": 4

}

NUMERICAL_FEATURES = [
    "avg_glucose_level",
    "age"


]

LABEL_KEY = "stroke"
# ============================


def convert_num_to_one_hot(label_tensor, num_labels=2):
    """
    Convert a label into a one-hot vector

    Args:
        label_tensor (int): label tensor (0 or 1)
        num_labels (int, optional): num of label. Defaults to 2.

    Returns:
        tf.Tensor: label tensor
    """

    one_hot_tensor = tf.one_hot(label_tensor, num_labels)
    return tf.reshape(one_hot_tensor, [-1, num_labels])


def replace_nan(tensor):
    """
    Replace N/A value with zero number

    Args:
        tensor (list): list data with na data that want to replace

    Returns:
        list with replaced nan value
    """
    tensor = tf.cast(tensor, tf.float64)
    return tf.where(
        tf.math.is_nan(tensor),
        tft.mean(tensor),
        tensor
    )


def transformed_name(text):
    """
    Change Input Text to Text + _xf

    Args:
        text (String) : Column name before transformed

    Returns :
        String : Transformed text
    """
    return f"{text}_xf"


def preprocessing_fn(inputs):
    """
    Preprocess Input into Transformed Features

    Args:
        inputs(dict) : Map from feature keys to raw features

    Returns:
        dict: map from features keys to transformed features
    """

    outputs = {}

    # For Categorical Feats
    for keys, values in CATEGORICAL_FEATURES.items():
        int_value = tft.compute_and_apply_vocabulary(
            inputs[keys], top_k=values + 1)
        outputs[transformed_name(keys)] = convert_num_to_one_hot(
            int_value, num_labels=values + 1)

    # For Num Feats
    for feature in NUMERICAL_FEATURES:
        inputs[feature] = replace_nan(inputs[feature])
        outputs[transformed_name(feature)] = tft.scale_to_0_1(inputs[feature])

    outputs[transformed_name(LABEL_KEY)] = tf.cast(inputs[LABEL_KEY], tf.int64)

    return outputs
