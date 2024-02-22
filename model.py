import torch
from diffusers import DiffusionPipeline

from configreader import config


class BaseModel:
    def create_image(self, prompt:str):
        raise NotImplementedError(f"needs to implemented create_image method in {self.__class__.__name__}")
    


class Model(BaseModel):

    def __init__(self, model_id=config['model']['model_id']):
        self.device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
        self.model = DiffusionPipeline.from_pretrained(model_id, revision="fp16", torch_dtype=torch.float32)
        self.model = self.model.to(self.device)

        self.steps = int(config['model']['steps'])
        self.scale = int(config['model']['scale'])
        self.num_images_per_prompt = int(config['model']['num_images'])

        #reproducibility
        seed = torch.randint(0, 10000, (1,)).item()
        self.generator = torch.Generator(device=self.device).manual_seed(seed)


    def create_image(self, prompt, neg_prompt="", width=int(config['image']['width']), height=int(config['image']['height'])):
        image =  self.model(prompt, negative_prompt=neg_prompt, 
                            width=width, height=height, 
                            num_inference_steps=self.steps,
                            guidance_scale=self.scale, 
                            num_images_per_prompt=self.num_images_per_prompt, 
                            generator=self.generator).images[0]
        return image