universe = vanilla
executable = electra_run_pretraining.sh
output = condor_out/electra_run_pretraining.out
error = condor_out/electra_run_pretraining.err
log = condor_out/electra_run_pretraining.log
should_transfer_files = IF_NEEDED
when_to_transfer_output = ON_EXIT
request_GPUs = 1
queue
