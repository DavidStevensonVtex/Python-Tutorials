# filecmp_cmp.py
import filecmp

print("common_file    :", end=" ")
print(
    filecmp.cmp("example/dir1/common_file", "example/dir2/common_file", shallow=True),
    end=" ",
)
print(
    filecmp.cmp("example/dir1/common_file", "example/dir2/common_file", shallow=False)
)

print("contents_differ:", end=" ")
print(
    filecmp.cmp(
        "example/dir1/contents_differ", "example/dir2/contents_differ", shallow=True
    ),
    end=" ",
)
print(
    filecmp.cmp(
        "example/dir1/contents_differ", "example/dir2/contents_differ", shallow=False
    )
)

print("identical      :", end=" ")
print(
    filecmp.cmp(
        "example/dir1/file_only_in_dir1", "example/dir1/file_only_in_dir1", shallow=True
    ),
    end=" ",
)
print(
    filecmp.cmp(
        "example/dir1/file_only_in_dir1",
        "example/dir1/file_only_in_dir1",
        shallow=False,
    )
)
