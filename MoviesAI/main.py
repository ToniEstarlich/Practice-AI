import torch
from diffusers import StableVideoDiffusionPipeline
from diffusers.utils import load_image, export_to_video


IMAGE_PATH = "input.jpg"
OUTPUT_PATH = "test_video.mp4"


print("Loading image...")

image = load_image(IMAGE_PATH)

# SVD works best with a 1024x576-ish landscape image.
image = image.resize((1024, 576))

print("Loading Stable Video Diffusion...")

pipe = StableVideoDiffusionPipeline.from_pretrained(
    "stabilityai/stable-video-diffusion-img2vid-xt",
    torch_dtype=torch.float32,
)

# Your GPU has only 1 GB VRAM, so force most/all computation onto CPU.
pipe.enable_model_cpu_offload()

print("Generating video...")

frames = pipe(
    image,
    num_frames=14,
    decode_chunk_size=1,
    motion_bucket_id=127,
    noise_aug_strength=0.1,
).frames[0]

print("Exporting video...")

export_to_video(
    frames,
    OUTPUT_PATH,
    fps=7,
)

print(f"Done! Video saved to: {OUTPUT_PATH}")