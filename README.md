# edith

edith: an edit-distance implementation with edit-path retrieval


## Usage

    import edith
    dst = edith.Distance(src, tgt)
    length = dst.calc()
    e_path = dst.editpath()

