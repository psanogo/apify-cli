            check=True,
            cwd=tmp_path / actor_name,
        )
        subprocess.run(  # noqa: ASYNC221, S603, S607
            ['apify', 'init', '-y', actor_name], capture_output=True, check=True, cwd=tmp_path / actor_name
        )

        build_process = subprocess.run(  # noqa: ASYNC221, S607
            ['apify', 'push', '-t', os.environ['APIFY_TEST_USER_API_TOKEN']],
            capture_output=True,
            check=True,
            cwd=tmp_path / actor_name,
        )
        # Get actor ID from build log
        actor_id_regexp = re.compile(r'https:\/\/console\.apify\.com\/actors\/(.*)#\/builds\/\d*\.\d*\.\d*')
    
