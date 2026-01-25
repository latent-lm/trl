from . import SFTConfig
from dataclasses import dataclass, field


@dataclass
class LTLMConfig(SFTConfig):
    """
    Configuration for Latent Language Model Trainer.
    """
    use_latent_ar: bool = False
