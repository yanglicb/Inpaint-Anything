# Stubbed out — these augmentation classes are only used during training,
# not inference. The original code imported removed albumentations APIs
# (DualIAATransform, to_tuple) and imgaug, which are incompatible with
# albumentations >= 2.0. Since we only need LaMa for inference, we
# replace with no-op stubs.

class IAAAffine2:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("IAAAffine2 is a training-only augmentation stub")

class IAAPerspective2:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("IAAPerspective2 is a training-only augmentation stub")
