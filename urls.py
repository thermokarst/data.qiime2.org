# ----------------------------------------------------------------------------
# Copyright (c) 2016-2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

# flake8: noqa

MAP = {
    # DISTRO
    'distro/core/aws-amis.txt':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/distro/core/aws-amis.txt',
    'distro/core/virtualbox-images.txt':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/distro/core/virtualbox-images.txt',
    'distro/core/2.0.6':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/distro/core/qiime206-1484941248.zip',
    'distro/core/qiime206.zip':  # LEGACY, we can probably delete this
        'https://s3-us-west-2.amazonaws.com/qiime2-data/distro/core/qiime206-1484941248.zip',
    'distro/core/2017.2':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/distro/core/qiime20172-1486602522.zip',
    'distro/core/qiime20172-1486602522.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/distro/core/qiime20172-1486602522.zip',
    'distro/core/qiime206-1479486933.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/distro/core/qiime206-1479486933.zip',
    'distro/core/qiime206-1484941248.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/distro/core/qiime206-1484941248.zip',
    'distro/core/qiime2-2017.2-conda-osx-64.txt':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/distro/core/qiime2-2017.2-conda-osx-64.txt',
    'distro/core/qiime2-2017.2-conda-linux-64.txt':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/distro/core/qiime2-2017.2-conda-linux-64.txt',

    # 2017.4 DISTRO
    'distro/core/qiime2-2017.4-conda-osx-64.txt':
        'https://raw.githubusercontent.com/qiime2/environment-files/master/2017.4/release/qiime2-2017.4-conda-osx-64.txt',
    'distro/core/qiime2-2017.4-conda-linux-64.txt':
        'https://raw.githubusercontent.com/qiime2/environment-files/master/2017.4/release/qiime2-2017.4-conda-linux-64.txt',
    'distro/core/2017.4':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/distro/core/qiime20174-1492814818.zip',
    'distro/core/qiime20174-1492814818.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/distro/core/qiime20174-1492814818.zip',

    # 2017.5 DISTRO
    'distro/core/qiime2-2017.5-conda-osx-64.txt':
        'https://raw.githubusercontent.com/qiime2/environment-files/master/2017.5/release/qiime2-2017.5-conda-osx-64.txt',
    'distro/core/qiime2-2017.5-conda-linux-64.txt':
        'https://raw.githubusercontent.com/qiime2/environment-files/master/2017.5/release/qiime2-2017.5-conda-linux-64.txt',
    'distro/core/2017.5':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/distro/core/qiime20175-1495755264.zip',
    'distro/core/qiime20175-1495755264.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/distro/core/qiime20175-1495755264.zip',

    # 2017.6 DISTRO
    'distro/core/qiime2-2017.6-conda-osx-64.txt':
        'https://raw.githubusercontent.com/qiime2/environment-files/master/2017.6/release/qiime2-2017.6-conda-osx-64.txt',
    'distro/core/qiime2-2017.6-conda-linux-64.txt':
        'https://raw.githubusercontent.com/qiime2/environment-files/master/2017.6/release/qiime2-2017.6-conda-linux-64.txt',
    # TODO: Update these
    'distro/core/2017.6':
        'https://purple.com',
    'distro/core/qiime20176-BUILD.zip':
        'https://purple.com',

    # 2.0.5
    '2.0.5/common/gg-13-8-99-515-806-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.5/common/gg-13-8-99-515-806-nb-classifier.qza',
    '2.0.5/tutorials/88soils/88soils-tutorial-demux-10p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.5/tutorials/88soils/88soils-tutorial-demux-10p.qza',
    '2.0.5/tutorials/88soils/88soils-tutorial-demux-1p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.5/tutorials/88soils/88soils-tutorial-demux-1p.qza',
    '2.0.5/tutorials/88soils/88soils-tutorial-demux-full.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.5/tutorials/88soils/88soils-tutorial-demux-full.qza',
    '2.0.5/tutorials/88soils/88soils-tutorial-raw-sequences.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.5/tutorials/88soils/88soils-tutorial-raw-sequences.qza',
    '2.0.5/tutorials/examples/feature-table.biom':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.5/tutorials/examples/feature-table.biom',
    '2.0.5/tutorials/fmt/fmt-tutorial-demux-1-10p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.5/tutorials/fmt/fmt-tutorial-demux-1-10p.qza',
    '2.0.5/tutorials/fmt/fmt-tutorial-demux-1-1p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.5/tutorials/fmt/fmt-tutorial-demux-1-1p.qza',
    '2.0.5/tutorials/fmt/fmt-tutorial-demux-1-full.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.5/tutorials/fmt/fmt-tutorial-demux-1-full.qza',
    '2.0.5/tutorials/fmt/fmt-tutorial-demux-2-10p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.5/tutorials/fmt/fmt-tutorial-demux-2-10p.qza',
    '2.0.5/tutorials/fmt/fmt-tutorial-demux-2-1p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.5/tutorials/fmt/fmt-tutorial-demux-2-1p.qza',
    '2.0.5/tutorials/fmt/fmt-tutorial-demux-2-full.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.5/tutorials/fmt/fmt-tutorial-demux-2-full.qza',
    '2.0.5/tutorials/fmt/fmt-tutorial-raw-sequences-1.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.5/tutorials/fmt/fmt-tutorial-raw-sequences-1.qza',
    '2.0.5/tutorials/fmt/fmt-tutorial-raw-sequences-2.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.5/tutorials/fmt/fmt-tutorial-raw-sequences-2.qza',
    '2.0.5/tutorials/moving-pictures/raw-sequences/barcodes.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.5/tutorials/moving-pictures/raw-sequences/barcodes.fastq.gz',
    '2.0.5/tutorials/moving-pictures/raw-sequences/sequences.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.5/tutorials/moving-pictures/raw-sequences/sequences.fastq.gz',

    # 2.0.6
    '2.0.6/common/gg-13-8-99-515-806-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/common/gg-13-8-99-515-806-nb-classifier.qza',
    '2.0.6/common/gg-13-8-99-full-length-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/common/gg-13-8-99-full-length-nb-classifier.qza',
    '2.0.6/common/silva-119-99-515-806-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/common/silva-119-99-515-806-nb-classifier.qza',
    '2.0.6/common/silva-119-99-full-length-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/common/silva-119-99-full-length-nb-classifier.qza',
    '2.0.6/tutorials/88soils/88soils-tutorial-demux-10p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/88soils/88soils-tutorial-demux-10p.qza',
    '2.0.6/tutorials/88soils/88soils-tutorial-demux-1p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/88soils/88soils-tutorial-demux-1p.qza',
    '2.0.6/tutorials/88soils/88soils-tutorial-demux-full.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/88soils/88soils-tutorial-demux-full.qza',
    '2.0.6/tutorials/88soils/88soils-tutorial-raw-sequences.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/88soils/88soils-tutorial-raw-sequences.qza',
    '2.0.6/tutorials/examples/feature-table.biom':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/examples/feature-table.biom',
    '2.0.6/tutorials/filtering-feature-tables/table.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/filtering-feature-tables/table.qza',
    '2.0.6/tutorials/fmt/fmt-tutorial-demux-1-10p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/fmt/fmt-tutorial-demux-1-10p.qza',
    '2.0.6/tutorials/fmt/fmt-tutorial-demux-1-1p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/fmt/fmt-tutorial-demux-1-1p.qza',
    '2.0.6/tutorials/fmt/fmt-tutorial-demux-1-full.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/fmt/fmt-tutorial-demux-1-full.qza',
    '2.0.6/tutorials/fmt/fmt-tutorial-demux-2-10p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/fmt/fmt-tutorial-demux-2-10p.qza',
    '2.0.6/tutorials/fmt/fmt-tutorial-demux-2-1p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/fmt/fmt-tutorial-demux-2-1p.qza',
    '2.0.6/tutorials/fmt/fmt-tutorial-demux-2-full.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/fmt/fmt-tutorial-demux-2-full.qza',
    '2.0.6/tutorials/fmt/fmt-tutorial-raw-sequences-1.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/fmt/fmt-tutorial-raw-sequences-1.qza',
    '2.0.6/tutorials/fmt/fmt-tutorial-raw-sequences-2.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/fmt/fmt-tutorial-raw-sequences-2.qza',
    '2.0.6/tutorials/importing-sequence-data/casava-18-single-end-demultiplexed.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/importing-sequence-data/casava-18-single-end-demultiplexed.zip',
    '2.0.6/tutorials/moving-pictures/raw-sequences/barcodes.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/moving-pictures/raw-sequences/barcodes.fastq.gz',
    '2.0.6/tutorials/moving-pictures/raw-sequences/sequences.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/moving-pictures/raw-sequences/sequences.fastq.gz',
    '2.0.6/tutorials/training-feature-classifiers/85_otu_taxonomy.txt':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/training-feature-classifiers/85_otu_taxonomy.txt',
    '2.0.6/tutorials/training-feature-classifiers/aligned_85_otu_sequences.fasta.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/training-feature-classifiers/aligned_85_otu_sequences.fasta.gz',
    '2.0.6/tutorials/training-feature-classifiers/rep-seqs.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/training-feature-classifiers/rep-seqs.qza',

    # 2017.2
    '2017.2/common/gg-13-8-99-515-806-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/common/gg-13-8-99-515-806-nb-classifier.qza',
    '2017.2/common/gg-13-8-99-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/common/gg-13-8-99-nb-classifier.qza',
    '2017.2/common/silva-119-99-515-806-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/common/silva-119-99-515-806-nb-classifier.qza',
    '2017.2/common/silva-119-99-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/common/silva-119-99-nb-classifier.qza',
    '2017.2/tutorials/atacama-soils/10p/barcodes.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/atacama-soils/10p/barcodes.fastq.gz',
    '2017.2/tutorials/atacama-soils/10p/forward.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/atacama-soils/10p/forward.fastq.gz',
    '2017.2/tutorials/atacama-soils/10p/reverse.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/atacama-soils/10p/reverse.fastq.gz',
    '2017.2/tutorials/atacama-soils/1p/barcodes.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/atacama-soils/1p/barcodes.fastq.gz',
    '2017.2/tutorials/atacama-soils/1p/forward.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/atacama-soils/1p/forward.fastq.gz',
    '2017.2/tutorials/atacama-soils/1p/reverse.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/atacama-soils/1p/reverse.fastq.gz',
    '2017.2/tutorials/filtering/distance-matrix.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/filtering/distance-matrix.qza',
    '2017.2/tutorials/filtering/table.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/filtering/table.qza',
    '2017.2/tutorials/fmt/fmt-tutorial-demux-1-10p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/fmt/fmt-tutorial-demux-1-10p.qza',
    '2017.2/tutorials/fmt/fmt-tutorial-demux-1-1p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/fmt/fmt-tutorial-demux-1-1p.qza',
    '2017.2/tutorials/fmt/fmt-tutorial-demux-2-10p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/fmt/fmt-tutorial-demux-2-10p.qza',
    '2017.2/tutorials/fmt/fmt-tutorial-demux-2-1p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/fmt/fmt-tutorial-demux-2-1p.qza',
    '2017.2/tutorials/importing-sequence-data/casava-18-paired-end-demultiplexed.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/importing-sequence-data/casava-18-paired-end-demultiplexed.zip',
    '2017.2/tutorials/importing-sequence-data/casava-18-single-end-demultiplexed.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/importing-sequence-data/casava-18-single-end-demultiplexed.zip',
    '2017.2/tutorials/importing-sequence-data/feature-table-v100.biom':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/importing-sequence-data/feature-table-v100.biom',
    '2017.2/tutorials/importing-sequence-data/feature-table-v210.biom':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/importing-sequence-data/feature-table-v210.biom',
    '2017.2/tutorials/moving-pictures/emp-single-end-sequences/barcodes.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/moving-pictures/emp-single-end-sequences/barcodes.fastq.gz',
    '2017.2/tutorials/moving-pictures/emp-single-end-sequences/sequences.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/moving-pictures/emp-single-end-sequences/sequences.fastq.gz',
    '2017.2/tutorials/training-feature-classifiers/85_otu_taxonomy.txt':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/training-feature-classifiers/85_otu_taxonomy.txt',
    '2017.2/tutorials/training-feature-classifiers/85_otus.fasta':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/training-feature-classifiers/85_otus.fasta',
    '2017.2/tutorials/training-feature-classifiers/rep-seqs.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/training-feature-classifiers/rep-seqs.qza',
    '2017.2/tutorials/atacama-soils/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/1xMP1EjKZDrzdKLnQr7LGVAY35ongxrreT28k0EACtfg/export?gid=0&format=tsv',
    '2017.2/tutorials/atacama-soils/sample_metadata':
        'https://docs.google.com/spreadsheets/d/1xMP1EjKZDrzdKLnQr7LGVAY35ongxrreT28k0EACtfg/edit?usp=sharing',
    '2017.2/tutorials/fmt/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/197f9kTKhcvcwqIjQaSkDHqsWeLO5jNN2_LlAN3NuadI/export?gid=0&format=tsv',
    '2017.2/tutorials/fmt/sample_metadata':
        'https://docs.google.com/spreadsheets/d/197f9kTKhcvcwqIjQaSkDHqsWeLO5jNN2_LlAN3NuadI/edit?usp=sharing',
    '2017.2/tutorials/moving-pictures/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/1WwCnhP7VbiVXY5-XHLoYAT-wAU68ItEF117TYJeQCrg/export?gid=0&format=tsv',
    '2017.2/tutorials/moving-pictures/sample_metadata':
        'https://docs.google.com/spreadsheets/d/1WwCnhP7VbiVXY5-XHLoYAT-wAU68ItEF117TYJeQCrg/edit?usp=sharing',

    # 2017.4
    '2017.4/common/gg-13-8-99-515-806-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/common/gg-13-8-99-515-806-nb-classifier.qza',
    '2017.4/common/gg-13-8-99-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/common/gg-13-8-99-nb-classifier.qza',
    '2017.4/common/silva-119-99-515-806-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/common/silva-119-99-515-806-nb-classifier.qza',
    '2017.4/common/silva-119-99-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/common/silva-119-99-nb-classifier.qza',
    '2017.4/tutorials/atacama-soils/10p/barcodes.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/tutorials/atacama-soils/10p/barcodes.fastq.gz',
    '2017.4/tutorials/atacama-soils/10p/forward.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/tutorials/atacama-soils/10p/forward.fastq.gz',
    '2017.4/tutorials/atacama-soils/10p/reverse.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/tutorials/atacama-soils/10p/reverse.fastq.gz',
    '2017.4/tutorials/atacama-soils/1p/barcodes.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/tutorials/atacama-soils/1p/barcodes.fastq.gz',
    '2017.4/tutorials/atacama-soils/1p/forward.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/tutorials/atacama-soils/1p/forward.fastq.gz',
    '2017.4/tutorials/atacama-soils/1p/reverse.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/tutorials/atacama-soils/1p/reverse.fastq.gz',
    '2017.4/tutorials/exporting/feature-table.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/tutorials/exporting/feature-table.qza',
    '2017.4/tutorials/exporting/unrooted-tree.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/tutorials/exporting/unrooted-tree.qza',
    '2017.4/tutorials/filtering/distance-matrix.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/tutorials/filtering/distance-matrix.qza',
    '2017.4/tutorials/filtering/table.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/tutorials/filtering/table.qza',
    '2017.4/tutorials/fmt/fmt-tutorial-demux-1-10p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/tutorials/fmt/fmt-tutorial-demux-1-10p.qza',
    '2017.4/tutorials/fmt/fmt-tutorial-demux-1-1p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/tutorials/fmt/fmt-tutorial-demux-1-1p.qza',
    '2017.4/tutorials/fmt/fmt-tutorial-demux-2-10p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/tutorials/fmt/fmt-tutorial-demux-2-10p.qza',
    '2017.4/tutorials/fmt/fmt-tutorial-demux-2-1p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/tutorials/fmt/fmt-tutorial-demux-2-1p.qza',
    '2017.4/tutorials/importing/aligned-sequences.fna':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/tutorials/importing/aligned-sequences.fna',
    '2017.4/tutorials/importing/casava-18-paired-end-demultiplexed.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/tutorials/importing/casava-18-paired-end-demultiplexed.zip',
    '2017.4/tutorials/importing/casava-18-single-end-demultiplexed.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/tutorials/importing/casava-18-single-end-demultiplexed.zip',
    '2017.4/tutorials/importing/feature-table-v100.biom':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/tutorials/importing/feature-table-v100.biom',
    '2017.4/tutorials/importing/feature-table-v210.biom':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/tutorials/importing/feature-table-v210.biom',
    '2017.4/tutorials/importing/pe-64-manifest':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/tutorials/importing/pe-64-manifest',
    '2017.4/tutorials/importing/pe-64.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/tutorials/importing/pe-64.zip',
    '2017.4/tutorials/importing/se-33-manifest':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/tutorials/importing/se-33-manifest',
    '2017.4/tutorials/importing/se-33.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/tutorials/importing/se-33.zip',
    '2017.4/tutorials/importing/sequences.fna':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/tutorials/importing/sequences.fna',
    '2017.4/tutorials/importing/unrooted-tree.tre':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/tutorials/importing/unrooted-tree.tre',
    '2017.4/tutorials/moving-pictures/emp-single-end-sequences/barcodes.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/tutorials/moving-pictures/emp-single-end-sequences/barcodes.fastq.gz',
    '2017.4/tutorials/moving-pictures/emp-single-end-sequences/sequences.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/tutorials/moving-pictures/emp-single-end-sequences/sequences.fastq.gz',
    '2017.4/tutorials/training-feature-classifiers/85_otu_taxonomy.txt':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/tutorials/training-feature-classifiers/85_otu_taxonomy.txt',
    '2017.4/tutorials/training-feature-classifiers/85_otus.fasta':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/tutorials/training-feature-classifiers/85_otus.fasta',
    '2017.4/tutorials/training-feature-classifiers/rep-seqs.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.4/tutorials/training-feature-classifiers/rep-seqs.qza',
    '2017.4/tutorials/atacama-soils/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/1pDrxXdv87ln9WldEIBCG93eSXf3gfxNXlkeLodBlnOI/export?gid=0&format=tsv',
    '2017.4/tutorials/atacama-soils/sample_metadata':
        'https://docs.google.com/spreadsheets/d/1pDrxXdv87ln9WldEIBCG93eSXf3gfxNXlkeLodBlnOI/edit?usp=sharing',
    '2017.4/tutorials/fmt/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/1Z2Egv1j6MrZntlOJsRfpspHEWFbHCDZxrWpKV5Fh8gU/export?gid=0&format=tsv',
    '2017.4/tutorials/fmt/sample_metadata':
        'https://docs.google.com/spreadsheets/d/1Z2Egv1j6MrZntlOJsRfpspHEWFbHCDZxrWpKV5Fh8gU/edit?usp=sharing',
    '2017.4/tutorials/moving-pictures/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/1kyK1g5e2KM7akG3Nc2XshkdGSlpBWOVGHmLorNthzfY/export?gid=0&format=tsv',
    '2017.4/tutorials/moving-pictures/sample_metadata':
        'https://docs.google.com/spreadsheets/d/1kyK1g5e2KM7akG3Nc2XshkdGSlpBWOVGHmLorNthzfY/edit?usp=sharing',

    # 2017.5
    '2017.5/common/gg-13-8-99-515-806-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/common/gg-13-8-99-515-806-nb-classifier.qza',
    '2017.5/common/gg-13-8-99-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/common/gg-13-8-99-nb-classifier.qza',
    '2017.5/common/silva-119-99-515-806-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/common/silva-119-99-515-806-nb-classifier.qza',
    '2017.5/common/silva-119-99-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/common/silva-119-99-nb-classifier.qza',
    '2017.5/tutorials/atacama-soils/10p/barcodes.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/tutorials/atacama-soils/10p/barcodes.fastq.gz',
    '2017.5/tutorials/atacama-soils/10p/forward.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/tutorials/atacama-soils/10p/forward.fastq.gz',
    '2017.5/tutorials/atacama-soils/10p/reverse.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/tutorials/atacama-soils/10p/reverse.fastq.gz',
    '2017.5/tutorials/atacama-soils/1p/barcodes.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/tutorials/atacama-soils/1p/barcodes.fastq.gz',
    '2017.5/tutorials/atacama-soils/1p/forward.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/tutorials/atacama-soils/1p/forward.fastq.gz',
    '2017.5/tutorials/atacama-soils/1p/reverse.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/tutorials/atacama-soils/1p/reverse.fastq.gz',
    '2017.5/tutorials/exporting/feature-table.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/tutorials/exporting/feature-table.qza',
    '2017.5/tutorials/exporting/unrooted-tree.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/tutorials/exporting/unrooted-tree.qza',
    '2017.5/tutorials/filtering/distance-matrix.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/tutorials/filtering/distance-matrix.qza',
    '2017.5/tutorials/filtering/table.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/tutorials/filtering/table.qza',
    '2017.5/tutorials/fmt/fmt-tutorial-demux-1-10p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/tutorials/fmt/fmt-tutorial-demux-1-10p.qza',
    '2017.5/tutorials/fmt/fmt-tutorial-demux-1-1p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/tutorials/fmt/fmt-tutorial-demux-1-1p.qza',
    '2017.5/tutorials/fmt/fmt-tutorial-demux-2-10p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/tutorials/fmt/fmt-tutorial-demux-2-10p.qza',
    '2017.5/tutorials/fmt/fmt-tutorial-demux-2-1p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/tutorials/fmt/fmt-tutorial-demux-2-1p.qza',
    '2017.5/tutorials/importing/aligned-sequences.fna':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/tutorials/importing/aligned-sequences.fna',
    '2017.5/tutorials/importing/casava-18-paired-end-demultiplexed.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/tutorials/importing/casava-18-paired-end-demultiplexed.zip',
    '2017.5/tutorials/importing/casava-18-single-end-demultiplexed.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/tutorials/importing/casava-18-single-end-demultiplexed.zip',
    '2017.5/tutorials/importing/feature-table-v100.biom':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/tutorials/importing/feature-table-v100.biom',
    '2017.5/tutorials/importing/feature-table-v210.biom':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/tutorials/importing/feature-table-v210.biom',
    '2017.5/tutorials/importing/pe-64-manifest':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/tutorials/importing/pe-64-manifest',
    '2017.5/tutorials/importing/pe-64.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/tutorials/importing/pe-64.zip',
    '2017.5/tutorials/importing/se-33-manifest':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/tutorials/importing/se-33-manifest',
    '2017.5/tutorials/importing/se-33.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/tutorials/importing/se-33.zip',
    '2017.5/tutorials/importing/sequences.fna':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/tutorials/importing/sequences.fna',
    '2017.5/tutorials/importing/unrooted-tree.tre':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/tutorials/importing/unrooted-tree.tre',
    '2017.5/tutorials/moving-pictures/emp-single-end-sequences/barcodes.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/tutorials/moving-pictures/emp-single-end-sequences/barcodes.fastq.gz',
    '2017.5/tutorials/moving-pictures/emp-single-end-sequences/sequences.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/tutorials/moving-pictures/emp-single-end-sequences/sequences.fastq.gz',
    '2017.5/tutorials/training-feature-classifiers/85_otu_taxonomy.txt':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/tutorials/training-feature-classifiers/85_otu_taxonomy.txt',
    '2017.5/tutorials/training-feature-classifiers/85_otus.fasta':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/tutorials/training-feature-classifiers/85_otus.fasta',
    '2017.5/tutorials/training-feature-classifiers/rep-seqs.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.5/tutorials/training-feature-classifiers/rep-seqs.qza',
    '2017.5/tutorials/atacama-soils/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/1GRaNc-Ik7_4K45EQjCjrML7dadxoz6l-w8CF4I4T7Ug/export?gid=0&format=tsv',
    '2017.5/tutorials/atacama-soils/sample_metadata':
        'https://docs.google.com/spreadsheets/d/1GRaNc-Ik7_4K45EQjCjrML7dadxoz6l-w8CF4I4T7Ug/edit?usp=sharing',
    '2017.5/tutorials/fmt/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/1kv1pomvbr3WQiEUA8P2N6zyVHkue4XXRI_U_3UmJVvw/export?gid=0&format=tsv',
    '2017.5/tutorials/fmt/sample_metadata':
        'https://docs.google.com/spreadsheets/d/1kv1pomvbr3WQiEUA8P2N6zyVHkue4XXRI_U_3UmJVvw/edit?usp=sharing',
    '2017.5/tutorials/moving-pictures/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/1_cDVn4B1wjzxdirkSxoEvOEmWPGn0XyCqbQGpeyg4Uc/export?gid=0&format=tsv',
    '2017.5/tutorials/moving-pictures/sample_metadata':
        'https://docs.google.com/spreadsheets/d/1_cDVn4B1wjzxdirkSxoEvOEmWPGn0XyCqbQGpeyg4Uc/edit?usp=sharing',

    # 2017.6
    '2017.6/common/gg-13-8-99-515-806-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/common/gg-13-8-99-515-806-nb-classifier.qza',
    '2017.6/common/gg-13-8-99-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/common/gg-13-8-99-nb-classifier.qza',
    '2017.6/common/silva-119-99-515-806-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/common/silva-119-99-515-806-nb-classifier.qza',
    '2017.6/common/silva-119-99-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/common/silva-119-99-nb-classifier.qza',
    '2017.6/tutorials/atacama-soils/10p/barcodes.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/atacama-soils/10p/barcodes.fastq.gz',
    '2017.6/tutorials/atacama-soils/10p/forward.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/atacama-soils/10p/forward.fastq.gz',
    '2017.6/tutorials/atacama-soils/10p/reverse.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/atacama-soils/10p/reverse.fastq.gz',
    '2017.6/tutorials/atacama-soils/1p/barcodes.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/atacama-soils/1p/barcodes.fastq.gz',
    '2017.6/tutorials/atacama-soils/1p/forward.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/atacama-soils/1p/forward.fastq.gz',
    '2017.6/tutorials/atacama-soils/1p/reverse.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/atacama-soils/1p/reverse.fastq.gz',
    '2017.6/tutorials/exporting/feature-table.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/exporting/feature-table.qza',
    '2017.6/tutorials/exporting/unrooted-tree.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/exporting/unrooted-tree.qza',
    '2017.6/tutorials/filtering/distance-matrix.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/filtering/distance-matrix.qza',
    '2017.6/tutorials/filtering/table.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/filtering/table.qza',
    '2017.6/tutorials/fmt/fmt-tutorial-demux-1-10p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/fmt/fmt-tutorial-demux-1-10p.qza',
    '2017.6/tutorials/fmt/fmt-tutorial-demux-1-1p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/fmt/fmt-tutorial-demux-1-1p.qza',
    '2017.6/tutorials/fmt/fmt-tutorial-demux-2-10p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/fmt/fmt-tutorial-demux-2-10p.qza',
    '2017.6/tutorials/fmt/fmt-tutorial-demux-2-1p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/fmt/fmt-tutorial-demux-2-1p.qza',
    '2017.6/tutorials/importing/aligned-sequences.fna':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/importing/aligned-sequences.fna',
    '2017.6/tutorials/importing/casava-18-paired-end-demultiplexed.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/importing/casava-18-paired-end-demultiplexed.zip',
    '2017.6/tutorials/importing/casava-18-single-end-demultiplexed.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/importing/casava-18-single-end-demultiplexed.zip',
    '2017.6/tutorials/importing/feature-table-v100.biom':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/importing/feature-table-v100.biom',
    '2017.6/tutorials/importing/feature-table-v210.biom':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/importing/feature-table-v210.biom',
    '2017.6/tutorials/importing/pe-64-manifest':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/importing/pe-64-manifest',
    '2017.6/tutorials/importing/pe-64.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/importing/pe-64.zip',
    '2017.6/tutorials/importing/se-33-manifest':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/importing/se-33-manifest',
    '2017.6/tutorials/importing/se-33.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/importing/se-33.zip',
    '2017.6/tutorials/importing/sequences.fna':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/importing/sequences.fna',
    '2017.6/tutorials/importing/unrooted-tree.tre':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/importing/unrooted-tree.tre',
    '2017.6/tutorials/moving-pictures/emp-single-end-sequences/barcodes.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/moving-pictures/emp-single-end-sequences/barcodes.fastq.gz',
    '2017.6/tutorials/moving-pictures/emp-single-end-sequences/sequences.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/moving-pictures/emp-single-end-sequences/sequences.fastq.gz',
    '2017.6/tutorials/metadata/faith_pd_vector.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/metadata/faith_pd_vector.qza',
    '2017.6/tutorials/metadata/rep-seqs.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/metadata/rep-seqs.qza',
    '2017.6/tutorials/metadata/taxonomy.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/metadata/taxonomy.qza',
    '2017.6/tutorials/metadata/unweighted_unifrac_pcoa_results.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/metadata/unweighted_unifrac_pcoa_results.qza',
    '2017.6/tutorials/training-feature-classifiers/85_otu_taxonomy.txt':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/training-feature-classifiers/85_otu_taxonomy.txt',
    '2017.6/tutorials/training-feature-classifiers/85_otus.fasta':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/training-feature-classifiers/85_otus.fasta',
    '2017.6/tutorials/training-feature-classifiers/rep-seqs.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.6/tutorials/training-feature-classifiers/rep-seqs.qza',
    '2017.6/tutorials/atacama-soils/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/1RskGBPAx6ODMh882F1DbhFX7-HDzcXWi9ljZltuaDe0/export?gid=0&format=tsv',
    '2017.6/tutorials/atacama-soils/sample_metadata':
        'https://docs.google.com/spreadsheets/d/1RskGBPAx6ODMh882F1DbhFX7-HDzcXWi9ljZltuaDe0/edit?usp=sharing',
    '2017.6/tutorials/fmt/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/1bKUwBXZju3wBQ29lh5MbM7Mu8XSE6JbG3DbMuSyBjYw/export?gid=0&format=tsv',
    '2017.6/tutorials/fmt/sample_metadata':
        'https://docs.google.com/spreadsheets/d/1bKUwBXZju3wBQ29lh5MbM7Mu8XSE6JbG3DbMuSyBjYw/edit?usp=sharing',
    '2017.6/tutorials/moving-pictures/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/1suEU6qcWbGHB09Nj7smBfW3v4Yl8_O6lTEI-GYWUltY/export?gid=0&format=tsv',
    '2017.6/tutorials/moving-pictures/sample_metadata':
        'https://docs.google.com/spreadsheets/d/1suEU6qcWbGHB09Nj7smBfW3v4Yl8_O6lTEI-GYWUltY/edit?usp=sharing',
}
