{
  'includes': [
    '../../../gyp/common.gypi',
  ],
  'targets': [
    { 'target_name': 'iosapp',
      'product_name': 'Mapbox GL',
      'type': 'executable',
      'product_extension': 'app',
      'mac_bundle': 1,
      'mac_bundle_resources': [
        '<!@(find ./img -type f)',
      ],

      'dependencies': [
        '../../../mbgl.gyp:bundle_styles',
        '../../../mbgl.gyp:<(core_library)',
        '../../../mbgl.gyp:<(platform_library)',
        '../../../mbgl.gyp:<(storage_library)',
        '../mbgl-cocoa.gyp:mbgl-cocoa',
      ],

      'sources': [
        'main.m',
        'MBXAppDelegate.h',
        'MBXAppDelegate.m',
        'MBXViewController.h',
        'MBXViewController.mm',
        '../../../platform/darwin/settings_nsuserdefaults.mm',
        '../../../platform/darwin/Reachability.m',
      ],

      'variables' : {
        'ldflags': [
          '-framework SystemConfiguration', # For NSUserDefaults and Reachability
        ],
      },

      'xcode_settings': {
        'SDKROOT': 'iphoneos',
        'SUPPORTED_PLATFORMS': 'iphonesimulator iphoneos',
        'INFOPLIST_FILE': 'app-info.plist',
        'TARGETED_DEVICE_FAMILY': '1,2',
        'COMBINE_HIDPI_IMAGES': 'NO', # don't merge @2x.png images into .tiff files
        'CLANG_ENABLE_OBJC_ARC': 'YES',
        'OTHER_LDFLAGS': [ '<@(ldflags)' ],
      },

      'configurations': {
        'Debug': {
          'xcode_settings': {
            'CODE_SIGN_IDENTITY': 'iPhone Developer',
          },
        },
        'Release': {
          'xcode_settings': {
            'CODE_SIGN_IDENTITY': 'iPhone Distribution',
            'ARCHS': [ "armv7", "armv7s", "arm64", "i386", "x86_64" ],
          },
        },
      },
    }
  ]
}
