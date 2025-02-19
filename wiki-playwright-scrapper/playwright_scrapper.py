from playwright.sync_api import sync_playwright
import sys
import os

def fetch_stats(page, url):
    """
    Fetch stats from the given URL using Playwright page.
    """
    try:
        page.set_default_timeout(1700)
        page.goto(url, wait_until="domcontentloaded")
        stats = {}

        # Locate stats on the page
        stats['hp'] = page.locator("text=HP:").locator("xpath=following-sibling::*").nth(0).text_content().strip()
        stats['mp'] = page.locator("text=MP:").locator("xpath=following-sibling::*").nth(0).text_content().strip()
        stats['patk'] = page.locator("text=P.Atk.:").locator("xpath=following-sibling::*").nth(0).text_content().strip()
        stats['matk'] = page.locator("text=M.Atk.:").locator("xpath=following-sibling::*").nth(0).text_content().strip()
        stats['pdef'] = page.locator("text=P.Def.:").locator("xpath=following-sibling::*").nth(0).text_content().strip()
        stats['mdef'] = page.locator("text=M.Def.:").locator("xpath=following-sibling::*").nth(0).text_content().strip()

        return stats
    except Exception as e:
        print(f"Error fetching stats from {url}: {e}")
        return None

def write_update_statement(output_file, npc_id, stats):
    """
    Write the SQL UPDATE statement to the output file.
    """
    with open(output_file, "a") as file:
        sql = (
            f"UPDATE npc SET hp = {stats['hp']}, mp = {stats['mp']}, "
            f"patk = {stats['patk']}, matk = {stats['matk']}, "
            f"pdef = {stats['pdef']}, mdef = {stats['mdef']} "
            f"WHERE id = {npc_id};\n"
        )
        file.write(sql)
        print(f"Written SQL for ID {npc_id}")

def main(start_id, end_id, summon_name, output_file):
    """
    Main function to scrape stats and generate SQL statements.
    """
    base_url = "https://lineage2wiki.com/interlude/monster"

    # Ensure the output file is empty before starting
    if os.path.exists(output_file):
        os.remove(output_file)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for npc_id in range(start_id, end_id + 1):
            url = f"{base_url}/{npc_id}/{summon_name}"
            print(f"Processing ID {npc_id}: {url}")

            stats = fetch_stats(page, url)
            if stats:
                write_update_statement(output_file, npc_id, stats)
            else:
                print(f"Skipping ID {npc_id} due to missing or invalid data.")

        browser.close()

    print(f"Process completed. SQL statements written to {output_file}.")

if __name__ == "__main__":
    # Ensure proper arguments are passed
    if len(sys.argv) != 5:
        print("Usage: python playwright_sql_scraper.py <start_id> <end_id> <summon_name> <output_file>")
        sys.exit(1)

    start_id = int(sys.argv[1])
    end_id = int(sys.argv[2])
    summon_name = sys.argv[3]
    output_file = sys.argv[4]

    if start_id > end_id:
        print("Error: start_id must be less than or equal to end_id.")
        sys.exit(1)

    main(start_id, end_id, summon_name, output_file)
