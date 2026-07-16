
"""
Model Comparison Utilities
"""

import pandas as pd


def compare_models():

    comparison = pd.DataFrame({

        "Metric": [

            "Model",
            "mAP@50",
            "Precision",
            "Recall",
            "Inference Time (ms)"

        ],

        "YOLOv8": [

            "YOLOv8n",
            0.82,
            0.84,
            0.80,
            18

        ],

        "Faster R-CNN": [

            "Faster R-CNN",
            0.79,
            0.81,
            0.77,
            65

        ]

    })

    return comparison
