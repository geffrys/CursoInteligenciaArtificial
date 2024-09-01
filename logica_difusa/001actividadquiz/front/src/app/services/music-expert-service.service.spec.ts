import { TestBed } from '@angular/core/testing';

import { MusicExpertServiceService } from './music-expert-service.service';

describe('MusicExpertServiceService', () => {
  let service: MusicExpertServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(MusicExpertServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
