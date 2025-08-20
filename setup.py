from setuptools import setup, find_packages

setup(
    name="u2net",
    version="0.1",
    description="U²-Net: Going Deeper with Nested U-Structure for Salient Object Detection",
    author="Xuebin Qin",
    url="https://github.com/xuebinqin/U-2-Net",
    packages=find_packages(include=["u2net", "u2net.*"]),
    install_requires=[
        "torch",
        "torchvision",
        "opencv-python",
        "Pillow",
        "scipy",
        "requests"
    ],
    python_requires=">=3.6",
)
