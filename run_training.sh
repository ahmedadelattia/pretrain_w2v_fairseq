base_model=$1
base_model=${base_model%.pt}
restore_file=$2
#wandb project name ends with the model name without .pt
wandb_project_name=w2v2_pretraining_trial_$base_model
#remove .pt from wandb project name
#config is wav2vec2_base_librispeech if base exists in base_model and wav2vec2_large if large exists in base_model

config_name=wav2vec2_large
# mkdir $base_model-pretraining
# cd $base_model-pretraining

echo "base_model: $base_model"
echo "wandb_project_name: $wandb_project_name"
echo "config_name: $config_name"

fairseq-hydra-train \
  task.data=/home/ahmed/Research/Projects/pretrain_w2v_fairseq/manifist \

  common.wandb_project=$wandb_project_name \
  task._name=audio_pretraining \
  common.log_interval=200 \
  common.log_format=tqdm \
  dataset.max_tokens=3000000 \
  checkpoint.save_dir=ckpts \
  checkpoint.restore_file=$restore_file \
  +optimization.update_freq='[1]' \
  optimization.clip_norm=0.5 \
  checkpoint.reset_optimizer=true \
  distributed_training.distributed_world_size=1 \
  --config-dir config/pretraining/ \
  --config-name $config_name \

    # common.user_dir=/path/to/custom_task/directory \

