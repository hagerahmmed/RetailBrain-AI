"""
Visualization Utilities

This module provides helper functions for visualizing
object detection results.
"""


def draw_detection(result):
    """
    Draw bounding boxes, class labels, and confidence scores
    on the detected image.

    Parameters
    ----------
    result : ultralytics.engine.results.Results
        YOLO detection result.

    Returns
    -------
    numpy.ndarray
        Annotated image.
    """

    detected_image = result.plot()

    return detected_image
