``` 
**************   Example    **************


from magicmodel import tools as mt

# global
mel = "ckpt/mel/mel_batch.pth"
voc = "ckpt/vocoder_mid/voc_mid.pth"
voc_config = "ckpt/vocoder_mid/config.json"

mel_cml_mgm = "mel_mgm.mlpackage"
voc_cml_mgm = "voc_mgm.mlpackage"
mel_mgmc = "mel_8bits_mgmc.mlpackage"
voc_mgmc =  "voc_8bits_mgmc.mlpackage"
mel_mgmcc = "mel_8bits_mgmc.mlmodelc"
voc_mgmcc =  "voc_8bits_mgmc.mlmodelc"

result_save_to = "result_save.wav"

ppg = "ppg_saved_320_fp16.npz"
F0 = "F0_saved_320_fp16.npz"
embedding = "embedding_saved_320_fp16.npy"
wave_in = "wav_in_saved_320_fp16.npz"

if __name__ == "__main__":
    
    # 模型准换
    mt.convert_mel(mel, mel_cml_mgm)
    mt.convert_voc(voc, voc_config, voc_cml_mgm)

    # 模型压缩
    mt.compress_model(mel_cml_mgm, mel_mgmc, 8)
    mt.compress_model(voc_cml_mgm, voc_mgmc, 8)

    # 编译模型
    mt.compile_model(mel_mgmc, ".")
    mt.compile_model(voc_mgmc, ".")

    # # 推理验证
    mt.svc_infer_dump(mel_mgmcc, voc_mgmcc, ppg, F0, embedding, wave_in, result_save_to)

```