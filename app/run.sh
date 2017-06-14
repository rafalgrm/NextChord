BUNDLE_PATH=/Users/fib1123/Desktop/cognitive/NextChord/app/models/basic_rnn.mag
CONFIG='basic_rnn'

melody_rnn_generate \
--config=${CONFIG} \
--bundle_file=${BUNDLE_PATH} \
--output_dir=out \
--num_outputs=15 \
--num_steps=256 \
--primer_melody="[60]"
