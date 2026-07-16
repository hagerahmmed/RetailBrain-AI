"""
Prediction Utilities
"""

import tempfile
import time


def run_prediction(model, image):

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".jpg"
    ) as temp:

        image.save(temp.name)

        start = time.time()

        results = model.predict(

            source=temp.name,

            conf=0.25,

            verbose=False

        )

        end = time.time()

    inference_time = end - start

    return results[0], inference_time
