universe = vanilla
executable = electra_run_pretraining_eval.sh
output = condor_out/electra_run_pretraining_eval.out
error = condor_out/electra_run_pretraining_eval.err
log = condor_out/electra_run_pretraining_eval.log
should_transfer_files = IF_NEEDED
when_to_transfer_output = ON_EXIT
request_GPUs = 1
queue
