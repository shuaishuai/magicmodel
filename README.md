``` Example

import magicmodel as mm

# global
mel = "ckpt/mel/mel_batch.pth"
voc = "ckpt/vocoder_mid/voc_mid.pth"
voc_config = "ckpt/vocoder_mid/config.json"
mel_cml_mgm = "mel_mgm.mlpackage"
voc_cml_mgm = "voc_mgm.mlpackage"
mel_mgmc = "mel_8bits_mgmc.mlpackage"
voc_mgmc =  "voc_8bits_mgmc.mlpackage"
result_save_to = "result_save.wav"

ppg = "ppg_saved_320_fp16.npz"
F0 = "F0_saved_320_fp16.npz"


 # 模型准换
mm.convert_seg(mel, voc, voc_config, mel_cml_mgm, voc_cml_mgm)

# 模型压缩
mm.compress_models(mel_cml_mgm, voc_cml_mgm, 8, mel_mgmc, voc_mgmc)

# 推理验证
mm.coreml_seg_infer_dump(mel_mgmc, voc_mgmc, ppg, F0, "embedding_saved_320_fp16.npy", "wav_in_saved_320_fp16.npz", result_save_to)

```