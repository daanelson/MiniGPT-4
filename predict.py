from cog import BasePredictor, Input, Path
import torch
from PIL import Image
from minigpt4.models.mini_gpt4 import MiniGPT4

class Predictor(BasePredictor):
    def setup(self):
        """Load the model into memory to make running multiple predictions efficient"""
        self.model = MiniGPT4.from_pretrained("path/to/pretrained/checkpoint")
        self.model.eval()
        self.model.to("cuda")

    def preprocess(self, image: Image) -> torch.Tensor:
        """Preprocess the input image"""
        img = image.convert("RGB")
        img = img.resize((224, 224), Image.LANCZOS)
        img_tensor = torch.from_numpy(np.array(img)).permute(2, 0, 1).float() / 255.0
        img_tensor = img_tensor.unsqueeze(0).to("cuda")
        return img_tensor

    def postprocess(self, output: torch.Tensor) -> str:
        """Postprocess the model output"""
        return output

    @Input("image", type=Image, description="Input image")
    @Output("response", type=str, description="Generated response from the model")
    def predict(self, image: Image) -> str:
        """Run a single prediction on the model"""
        processed_image = self.preprocess(image)
        with torch.no_grad():
            output = self.model(processed_image)
        response = self.postprocess(output)
        return response