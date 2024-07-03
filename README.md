# PCB Card Defect Detection by Comparison

This project aims to detect defects in PCB (Printed Circuit Board) cards using image comparison techniques. The main goal is to identify differences between a reference PCB card and a test PCB card, which may indicate defects such as missing components or misplaced parts.

## Features

- **Image Comparison:** Utilizes various methods like histogram comparison, template matching, and structural similarity index (SSIM) to compare images.
- **Alignment:** Implements the Enhanced Correlation Coefficient (ECC) algorithm for aligning images and correcting small deformations.
- **Visualization:** Uses matplotlib to visualize results, including displaying reference images, aligned images, average images, and differences.
- **Thresholding and Noise Reduction:** Applies thresholding to highlight differences and uses morphological operations to reduce noise.
- **Edge Margin Handling:** Implements edge margin to prevent displaying edge differences as rectangles due to snapshot quality issues.

## Methods and Results

- **Histogram Comparison**

![resim](https://github.com/muhammeddincmdx/PCB-Card-Defect-Detection-by-Comparison/assets/54439858/84d393f1-ad52-4c7d-8367-801a53a8d14a)

![resim](https://github.com/muhammeddincmdx/PCB-Card-Defect-Detection-by-Comparison/assets/54439858/3dd61ae4-0697-4f74-9e8e-1e0d1beea34f)

- **Template Matching**

![resim](https://github.com/muhammeddincmdx/PCB-Card-Defect-Detection-by-Comparison/assets/54439858/4b32b408-b6fd-4343-ad6e-d6aa7dc08769)

![resim](https://github.com/muhammeddincmdx/PCB-Card-Defect-Detection-by-Comparison/assets/54439858/d44af392-470e-4337-a67e-6f5a697f26b6)

![resim](https://github.com/muhammeddincmdx/PCB-Card-Defect-Detection-by-Comparison/assets/54439858/f912a0d8-fd1a-400b-a948-828028fe7799)

- **Feature Matching**

![resim](https://github.com/muhammeddincmdx/PCB-Card-Defect-Detection-by-Comparison/assets/54439858/f100199a-6163-4a70-be0b-dca6985be715)

![resim](https://github.com/muhammeddincmdx/PCB-Card-Defect-Detection-by-Comparison/assets/54439858/45f03fc9-d8d3-4bc3-95ae-ccecf37d0190)

![resim](https://github.com/muhammeddincmdx/PCB-Card-Defect-Detection-by-Comparison/assets/54439858/410cceb1-ad99-4a24-a5dc-67820e389937)

- **Structural Similarity Index Measure (SSIM)**

![resim](https://github.com/muhammeddincmdx/PCB-Card-Defect-Detection-by-Comparison/assets/54439858/f2a46583-4823-45c8-8ad8-e4a41bc6c3e9)

![resim](https://github.com/muhammeddincmdx/PCB-Card-Defect-Detection-by-Comparison/assets/54439858/9018817c-bb39-44cd-98e5-f304bfa2c85c)

![resim](https://github.com/muhammeddincmdx/PCB-Card-Defect-Detection-by-Comparison/assets/54439858/bf807c94-f96d-43be-aa45-4fd4673ab139)

- **Absolute Difference**

![resim](https://github.com/muhammeddincmdx/PCB-Card-Defect-Detection-by-Comparison/assets/54439858/e316c561-25a1-4bbd-b036-0ff9e1ffd44b)

![resim](https://github.com/muhammeddincmdx/PCB-Card-Defect-Detection-by-Comparison/assets/54439858/59ee8831-c5ba-4f19-800e-5bd6f21bcc9a)

![resim](https://github.com/muhammeddincmdx/PCB-Card-Defect-Detection-by-Comparison/assets/54439858/ec37100a-2ad0-438f-86c5-d7ca34d196ac)

- **Substract**

![resim](https://github.com/muhammeddincmdx/PCB-Card-Defect-Detection-by-Comparison/assets/54439858/a2e6ab79-fc24-462d-b98b-272fdc1469f0)

![resim](https://github.com/muhammeddincmdx/PCB-Card-Defect-Detection-by-Comparison/assets/54439858/d0e335fe-88c6-4f02-8635-b0bfe76ca08f)

![resim](https://github.com/muhammeddincmdx/PCB-Card-Defect-Detection-by-Comparison/assets/54439858/acd5ed83-ba19-4817-8c1c-ebe1e54e4d4d)

- **main.py**-

![resim](https://github.com/muhammeddincmdx/PCB-Card-Defect-Detection-by-Comparison/assets/54439858/d68e1463-ac67-4d83-9b14-8c8fb3296244)

![resim](https://github.com/muhammeddincmdx/PCB-Card-Defect-Detection-by-Comparison/assets/54439858/73a8d7b9-b4b8-405d-806c-886ce6f0058b)

![resim](https://github.com/muhammeddincmdx/PCB-Card-Defect-Detection-by-Comparison/assets/54439858/3731ba2f-3f6d-469c-aa0d-c5f4cab9588a)

## Limitation

Not: This code may not yield optimal results with all images. In my scenario, I work with PCB cards and strive to capture clear snapshots, adjusting certain parameters manually to improve performance.


## Paper

https://medium.com/@me.muhammed.dinc/pcb-card-comparison-for-finding-defects-it-includes-python-image-comparison-method-f2cd3376e89e
