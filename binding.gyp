{
  'variables': 		
  {		
    'node_uwp_dll%': 'false',		
  },
  'targets': [
    {
      'target_name': 'serialport',
      'sources': [
        'src/serialport.cpp',
      ],
      'include_dirs': [
        '<!(node -e "require(\'nan\')")'
      ],
      'conditions': [
        ['OS=="win"',
          {
            'conditions': [
              ['node_uwp_dll!="true"',
                {
                  'sources': [
                    'src/serialport_win.cpp'
                  ],
                  'msvs_settings': {
                    'VCCLCompilerTool': {
                      'ExceptionHandling': '2',
                      'DisableSpecificWarnings': [ '4530', '4506' ],
                    },
                  },
                }
              ],
              ['node_uwp_dll=="true"',
                {
                  'sources': [
                    'src/serialport_uwp.cpp',
                  ],
                }
              ],
            ],
          },
        ],
        ['OS=="mac"',
          {
            'sources': [
              'src/serialport_unix.cpp',
              'src/read-poller.cpp',
            ],
            'xcode_settings': {
              'OTHER_LDFLAGS': [
                '-framework CoreFoundation -framework IOKit'
              ]
            }
          }
        ],
        ['OS!="win"',
          {
            'sources': [
              'src/serialport_unix.cpp',
              'src/read-poller.cpp',
            ],
          }
        ],
      ],
    }
  ],
}
