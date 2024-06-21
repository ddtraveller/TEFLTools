from bitcoinlib.services.services import Service

def main():
    try:
        # Initialize the Bitcoin service
        service = Service()

        # Get the estimated transaction fee in satoshis per KB for confirmation within 5 blocks
        fee = service.estimatefee(5)
        print("Estimated Transaction Fee:")
        print("  Satoshis per KB:", fee)

        # Get the latest block information
        latest_block = service.blockcount()
        block = service.getblock(latest_block)
        print("\nLatest Block:")
        print("  Block Height:", block.height)
        print("  Block Hash:", block.block_hash.hex())
        print("  Timestamp:", block.time)
        print("  Number of Transactions:", len(block.transactions))

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()