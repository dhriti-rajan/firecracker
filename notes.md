# Issue 1068: Create utils method for checking guest cmd output in the integration tests.
> In the integration tests there are multiple functions that execute a command
  on the guest and then compare the output with some expected values.  Like
  this one (https://github.com/firecracker-microvm/firecracker/blob/b8550cc749227565ad1e13ae4b99821c98239e94/tests/integration_tests/functional/test_cpu_features.py#L37).

> Create one `utils` method that does this and call it when needed instead of
  having a couple of similar methods scattered throughout the integration tests.

> See the comment at https://github.com/firecracker-microvm/firecracker/pull/1052#discussion_r277235971.

# Integration Tests

| status | file name | test name | rc check | stdout check | stderr check | rc code | stdout code | stderr code |
| ------ | --------- | --------- | -------- | ------------ | ------------ | ------- | ----------- | ----------- |
| DONE | fuctional/test_api.py | test_drive_io_engine | x | | x | | | |
| DONE | functional/test_api.py | test_api_version (NOT PASSING) | | | | | | |
| DONE | functional/test_balloon.py | make_guest_dirty_memory | x | | | x | x | x |
| DONE | functional/test_balloon.py | test_memory_scrub | x | | | | | |
| DONE | functional/test_cmd_line_start.py | test_config_start_and_mmds_with_api | | x | x | | x | |
| DONE | functional/test_cmd_line_start.py | test_with_config_and_metatdata_no_api | | x | x | | x | |
| DONE | functional/test_cpu_features.py | test_brand_string | | | x | | x | |
| DONE | functional/test_cpu_features.py | dump_msr_state_to_file | | | x | | x | |
| DONE | functional/test_cpu_features.py | test_cpu_wrmsr_snapshot | | | x | | | |
| DONE | functional/test_cpu_features.py | dump_cpuid_to_file | | | x | | x | |
| DONE | functional/test_drives.py | test_rescan_file | | | x | | | |
| DONE | functional/test_drives.py | test_patch_drive | | x | x | | x | |
| DONE | functional/test_drives.py | test_no_flush | | | x | | | |
| DONE | functional/test_drives.py | test_flush | | | x | | | |
| DONE | functional/test_drives.py | check_iops_limit | x | | x | | | x |
| DONE | functional/test_drives.py | _check_block_size | | x | x | | x | |
| DONE | functional/test_drives.py | _check_file_size | | x | x | | x | |
| DONE | functional/test_drives.py | _check_drives | | | x | | x | |
| DONE | functional/test_feat_parity.py | test_feat_parity_msr_arch_cap | | | | | x | x |
| DONE | functional/test_max_devices.py | test_attach_maximum_devices | x | | | | | |
| DONE | functional/test_max_vcpus.py | test_max_vcpus | | x | x | | x | |
| <mark>TODO</mark> | functional/test_mmds.py | test_guest_mmds_hang | | x | | | x | |
| <mark>TODO</mark> | functional/test_mmds.py | test_mmds_v2_negative | | | | | x | |
| <mark>TODO</mark> | functional/test_net_config_space.py | _send_data_g2h | x | | x | | | |
| <mark>TODO</mark> | functional/test_net_config_space.py | _change_guest_if_mac | | | | | | |
| <mark>TODO</mark> | functional/test_net_config_space.py | _get_net_mem_addr_base | x | | | | x | |
| DONE | functional/test_net.py | test_high_ingress_traffic | x | | | | | |
| DONE | functional/test_pause_resume.py | test_pause_resume | x | | | | | |
| DONE | functional/test_rate_limiter.py | _start_iperf_on_guest | | | | | | |
| DONE | functional/test_rate_limiter.py | _run_iperf_on_guest | | | x | | x | |
| <mark>TODO</mark> | functional/test_rtc.py | test_rtc | | | | | x | |
| DONE | functional/test_serial_io.py | test_serial_block | x | | | | | |
| DONE | functional/test_shut_down.py | test_reboot | | | | | | |
| DONE | functional/test_signals.py | test_handled_signals | | x | x | | x | |
| DONE | functional/test_snapshot_advanced.py | validate_all_devices | x | x | | | x | |
| DONE | functional/test_snapshot_advanced.py | create_snapshot_helper | x | | | | | |
| DONE | functional/test_snapshot_basic.py | _get_guest_drive_size | | | x | | x | |
| DONE | functional/test_snapshot_basic.py | test_cmp_full_and_first_diff_mem | x | | | | | |
| DONE | functional/test_snapshot_restore_cross_kernel.py | _test_mmds | x | | | | x | |
| DONE | functional/test_snapshot_restore_cross_kernel.py | test_snap_restore_from_artifacts | x | | | | | |
| DONE | functional/test_snapshot_version.py | _create_and_start_microvm_with_net_devices | x | | | | | |
| DONE | functional/test_topology.py | _check_cache_topology_arm | | | x | | x | |
| DONE | functional/test_uffd.py | create_snapshot | x | | | | | |
| DONE | functional/test_uffd.py | test_valid_handler | x | | | | | |
| DONE | functional/test_vsock.py | negative_test_host_connections | x | | | | | |
| <mark>TODO</mark> | performance/test_block_performance.py | run_fio | x | | x | | | |
| DONE | performance/test_network_tcp_throughput.py | produce_iperf_output | | | | | x | |
| <mark>TODO</mark> | performance/test_snapshot_perf.py | snapshot_resume_producer | x | | | | | |
| <mark>TODO</mark> | performance/test_snapshot_perf.py | test_older_snapshot_resume_latency | x | | | | | |
| <mark>TODO</mark> | performance/test_snapshot_perf.py | test_snapshot_resume_latency | x | | | | | |
| <mark>TODO</mark> | performance/test_snapshot_restore_performance.py | get_snap_restore_latency | x | | | | | |
| <mark>TODO</mark> | performance/test_vsock_throughput.py | produce_iperf_output | x | | x | | x | x |
| DONE | security/test_vulnerabilities.py | run_spectre_meltdown_checker_on_guest | x | | | | x | x |
| DONE | security/test_vulnerabilities.py | check_vulnerabilities_files_on_guest | x | | | | x | x |
