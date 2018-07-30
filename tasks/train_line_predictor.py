#!/usr/bin/env python

import os
os.environ["CUDA_VISIBLE_DEVICES"] = '0'

import numpy as np

from text_recognizer.datasets.emnist_lines import EmnistLinesDataset
from training.util import train_model

from text_recognizer.models.line_lstm_with_ctc import LineLstmWithCtc
MODEL = LineLstmWithCtc


def train():
    dataset = EmnistLinesDataset(max_overlap=0.4)
    dataset.load_or_generate_data()

    model = MODEL()
    train_model(model, dataset, epochs=20, batch_size=32)
    model.save_weights()

    model.evaluate(dataset.x_test, dataset.y_test)
    return model


if __name__ == '__main__':
    train()
