import speedtest

# Initialize speedtest
router_check = speedtest.Speedtest()

# Declare variables for download and upload speeds (bits per second) 
download_bps = router_check.download()
upload_bps = router_check.upload()

# Convert bps to mbps (1 mbps = 1,000,000 bps)
download_mbps = download_bps / 1_000_000
upload_mbps = upload_bps / 1_000_000

# Print download and upload speed
print("--- Speed Test Results ---\n" + "===============================")
print(f"Download Speed: ~{download_mbps:.2f} Mbps")
print(f"Upload Speed: ~{upload_mbps:.2f} Mbps")
print(f"Ping: {router_check.results.ping}")