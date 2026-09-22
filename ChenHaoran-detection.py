# my-detection.py
import jetson.inference
import jetson.utils


net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.1)

img_path1 = "/home/nvidia/jetson-inference/data/images/fruit_0.jpg"
img_path2 = "/home/nvidia/jetson-inference/data/images/fruit_1.jpg"


def run_detect(image_file):

    camera = jetson.utils.videoSource(image_file)
    img_gpu = camera.Capture()

    if img_gpu is None:
        print(f"❌错误：无法读取图片 {image_file}，检查路径是否正确！")
        return

    detections = net.Detect(img_gpu)  

    print(f"\n========== Detection result for {image_file} ==========")
    print(f"检测目标数量：{len(detections)}")
    for det in detections:
        print(f"ClassID:      {det.ClassID}")
        print(f"Confidence:   {det.Confidence:.6f}")
        print(f"Left:         {det.Left:.3f}")
        print(f"Top:          {det.Top:.3f}")
        print(f"Right:        {det.Right:.3f}")
        print(f"Bottom:       {det.Bottom:.3f}")
        print(f"Width:        {det.Width:.3f}")
        print(f"Height:       {det.Height:.3f}")
        print(f"Area:         {det.Area:.2f}")
        print(f"Center:       ({det.Center[0]:.3f}, {det.Center[1]:.3f})")
        print("-"*60)

    output_img_path = image_file.replace(".jpg","_out.jpg")
    jetson.utils.saveImage(output_img_path, img_gpu)
    print(f"✅输出带框图片：{output_img_path}")


run_detect(img_path1)
run_detect(img_path2)

