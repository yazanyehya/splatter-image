from .srn import SRNDataset

def get_dataset(cfg, name):
    if cfg.data.category == "cars" or cfg.data.category == "chairs":
        return SRNDataset(cfg, name)
    elif cfg.data.category == "hydrants" or cfg.data.category == "teddybears":
        return CO3DDataset(cfg, name)
    elif cfg.data.category == "nmr":
        return NMRDataset(cfg, name)
    elif cfg.data.category == "objaverse":
        return ObjaverseDataset(cfg, name)
    elif cfg.data.category == "gso":
        return GSODataset(cfg, name)
