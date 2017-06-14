BUNDLE_PATH=/home/rgrabianski/Pobrane/basic_rnn.mag
CONFIG='basic_rnn'

melody_rnn_generate \
--config=${CONFIG} \
--bundle_file=${BUNDLE_PATH} \
--output_dir=/tmp/melody_rnn/generated \
--num_outputs=15 \
--num_steps=256 \
--primer_melody="[60]"
