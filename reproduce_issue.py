import sys
try:
    print("Attempting to import tflite_support first...")
    import tflite_support
    print("SUCCESS: tflite_support imported")
except Exception as e:
    print(f"FAILED: tflite_support import failed: {e}")

try:
    print("Attempting to import tensorflow...")
    import tensorflow as tf
    print(f"SUCCESS: tensorflow {tf.__version__} imported")
except Exception as e:
    print(f"FAILED: tensorflow import failed: {e}")
