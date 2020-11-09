universe = vanilla
executable = electra_build_dataset.sh
output = condor_out/electra_build_dataset.out
error = condor_out/electra_build_dataset.err
log = condor_out/electra_build_dataset.log
should_transfer_files = IF_NEEDED
when_to_transfer_output = ON_EXIT
request_GPUs = 1
queue
