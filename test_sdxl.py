import torch
from compel import Compel

from diffusers import StableDiffusionPipeline, UniPCMultistepScheduler

pipe = StableDiffusionPipeline.from_pretrained(r"C:\Users\Youmi\Desktop\youmi\diffusion\models\stable-diffusion-xl-base-1.0")
pipe.scheduler = UniPCMultistepScheduler.from_config(pipe.scheduler.config)

compel_proc = Compel(tokenizer=pipe.tokenizer, text_encoder=pipe.text_encoder)

prompt = "a red cat playing with a ball++"
prompt_embeds = compel_proc(prompt)

generator = torch.Generator(device="cuda").manual_seed(33)

images = pipe(prompt_embeds=prompt_embeds, generator=generator, num_inference_steps=20).images[0]
